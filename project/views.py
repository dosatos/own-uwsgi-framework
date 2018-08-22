from web.shortcuts import render


def hello(request):
    template_path = "templates/hello.html"
    context = {"title": "Hello Page",
               "name": "World"}
    if request.method == "POST":
        context.update(request.get_args())
        return render(request, template_path, context)
    return render(request, template_path, context)
