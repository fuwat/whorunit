from django.shortcuts import render
from game.models import Game, Amd
import random
import urllib.parse
from plotly.offline import plot
import plotly.graph_objs as go


def home(request):
    image = random.choice(["https://s1.1zoom.me/b5050/861/Heroes_of_the_Storm_463603_1920x1080.jpg",
                           "https://wallpaperaccess.com/full/171177.jpg", "https://wallpapercave.com/wp/wp3538790.jpg",
                           "https://gamespot1.cbsistatic.com/uploads/original/1547/15470456/3050085-tekken7-3.jpg",
                           "https://d2ofqe7l47306o.cloudfront.net/games/1366x768/cuphead-sea-lady.jpg",
                           "https://hdwallsource.com/img/2017/12/rocket-league-video-game-hd-wallpaper-61728-63564-hd"
                           "-wallpapers.jpg",
                           "https://free4kwallpapers.com/uploads/originals/2020/08/31/fall-guys-wallpaper.png",
                           "https://wallpaperaccess.com/full/1648919.jpg",
                           "https://i.imgur.com/fFhyMVJ.jpg"])
    placeholder = Game.objects.order_by('?').first()
    latest = Game.objects.all()[:3]
    return render(request, "site.html", {'image': image, 'placeholder': '"' + placeholder.name + '"', 'latest': latest})


def results(request):
    if 'input' in request.GET:
        a = request.GET['input']
        gamez = Game.objects.filter(name__icontains=a)
    return render(request, "results.html", {'games': gamez, 'query': a})


def update_pie(fig):
    fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20, marker=dict(colors=["#69FF59", "#F34343"], line=dict(color="white", width=4)))
    fig.update_layout(width=400, height=400)


def game(request):
    q = urllib.parse.unquote(request.GET['q'])
    q = Game.objects.get(name=q)
    labels = ["who run it", "who don't run it"]
    values = [q.ram.percentage, 100 - q.ram.percentage]
    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    update_pie(fig)
    pie_ram = plot(fig, output_type='div')
    values = [q.nvidia.percentage + q.amd.percentage, 100 - q.nvidia.percentage - q.amd.percentage]
    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    update_pie(fig)
    pie_cpu = plot(fig, output_type='div')

    values = [q.cpu.percentage, 100 - q.cpu.percentage]
    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    update_pie(fig)
    pie_gpu = plot(fig, output_type='div')

    overall = round(((q.cpu.percentage + q.ram.percentage + q.amd.percentage + q.nvidia.percentage) / 3), 2)

    return render(request, "game.html",
                  {'game': q, 'pie_ram': pie_ram, 'pie_cpu': pie_cpu, 'pie_gpu': pie_gpu, 'all': overall})


def games(request):
    gamez = Game.objects.all().order_by('name')
    return render(request, "games.html", {'games': gamez})
