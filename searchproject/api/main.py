from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from UTILS import *
from database import Database


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
    

@app.get('/', response_class=HTMLResponse)
async def index(request: Request):
    context = {'request': request, 'firstmessage': 'search for something'}
    return templates.TemplateResponse('index.html', context)


@app.post("/")
async def get_fraze(request: Request):
    form = await request.form()
    fraze = form.get('fraze')
    if '--' in fraze:
        context = {'request': request, 'firstmessage': f'You are not allowed to search: {fraze}! '}
        return templates.TemplateResponse('index.html', context)
    else:
        results = Database().select_product(fraze)
        context = {'request': request, 'results': results, 'firstmessage': 'here are your results:'}
        return templates.TemplateResponse('index.html', context)


@app.post("/submit")
async def submit(request: Request):
    form = await request.form()
    category = form.get('category')
    results = Database().select_category_search(category)
    cat_name = Database().select_category_name(category)
    for i in cat_name:
        category = i[0]
    context = {'request': request, 'results': results, 'firstmessage': f'all results in: {category}'}
    return templates.TemplateResponse('index.html', context)
    

@app.get('/details/{id}', response_class=HTMLResponse)
async def get_product_id(request: Request, id: int):
    results = Database().select_details(id)
    comments_results = Database().select_comments(id)
    avg_rate = Database().select_avg_rating(id)
    context = {'request': request, 'results': results, 'comments': comments_results, 'id': id, 'avg_rate': avg_rate}
    return templates.TemplateResponse('prod-details.html', context)


@app.post('/submit-comment')
async def add_comment(request: Request):
    form = await request.form()
    username = form.get('username')
    rating = form.get('rating')
    comment = form.get('comment')
    id = form.get('id')
    print(username, rating, comment, id)
    if comment_not_null(comment):
        Database().insert_comment(username, rating, comment, id)
    else:
        comment = 'no comment'
        Database().insert_comment(username, rating, comment, id)
    return RedirectResponse('/', status_code=302)


@app.get('/payment', response_class=HTMLResponse)
async def payment(request: Request):
    context = {'request': request}
    return templates.TemplateResponse('payment.html', context)


@app.post('/payment')
async def get_card(request: Request):
    form = await request.form()
    name = form.get('input-name')
    CVV = form.get('CVV')
    numbers = form.get('card-numbers')
    is_allowed = form.get('save')
    if '--' in name or '--' in CVV or '--' in numbers:
        name = None
        CVV = None
        numbers = None
        context = {'request': request, 'message': "You can't use '--' in any of fields!"}
        return templates.TemplateResponse('payment.html', context)
    else:
        if all_valid(CVV, numbers) == True:
            if is_allowed:
                Database().insert_card_data(name, CVV, numbers)
            context = {'request': request}
            return templates.TemplateResponse('thanks-for-order.html', context)
        else:
            context = {'request': request, 'message': 'Wrong card data!'}
            return templates.TemplateResponse('payment.html', context)

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        app,
        reload_includes=["*.html", "*.css", "*.js"],
        reload_dirs=["../templates", "../templates/static", "../static"],
    )
