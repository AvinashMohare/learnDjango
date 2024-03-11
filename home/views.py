from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    peoples = [
        {'name' : 'Avinash', 'age' : 22},
        {'name' : 'Ajay', 'age' : 23},
        {'name' : 'Sandeep', 'age' : 24},
        {'name' : 'Sonu', 'age' : 5},
        {'name' : 'Shilpi', 'age' : 26},    
    ]

    text = """
    Lorem ipsum dolor sit amet consectetur adipisicing elit. Magnam, consequuntur recusandae, fuga aliquam iure dolore nam tenetur necessitatibus omnis earum fugit ab neque deserunt tempora autem ducimus quas, sint quo minus accusamus aut? Eligendi sunt nulla laboriosam dignissimos veritatis ipsam vitae rerum in perspiciatis fugit vero, quaerat ad neque atque enim, deleniti error mollitia natus ducimus! Alias reiciendis ad itaque repellendus modi deserunt placeat iusto dolorem asperiores, libero ex vel ab quas ut nemo obcaecati harum. Ea impedit facilis eveniet qui repudiandae odio asperiores corrupti ab autem. Maxime tempore et harum asperiores, nulla ut temporibus aut voluptatibus eligendi accusamus voluptas.
    """


    return render(request, "index.html", context={'page' : 'Home', 'peoples' : peoples, 'text' : text})


def about(request):
    context = {'page' : 'About'}
    return render(request, 'about.html', context)

def contact(request):
    context = {'page' : 'Contact'}
    return render(request, 'contact.html', context)

def success_page(request):
    return HttpResponse("<h1>This is a success page </h1>")