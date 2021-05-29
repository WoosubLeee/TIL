from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Reservation, Comment
from .forms import ReservationForm, CommentForm 

# Create your views here.
def create(request):
    # Q2-1
    # POST 방식의 요청이 들어오면
    if request.method == 'POST':
        # ReservationForm에 데이터를 받아
        form = ReservationForm(request.POST)
        # 데이터가 유효하다면
        if form.is_valid():
            # 데이터를 저장하고 /reservations/<pk>/ 경로로 redirect한다.
            form.save()
            return redirect('reservations:detail', form.instance.pk)
        # 유효하지 않을 경우 아래에서 오류메시지와 함께 render를 return하게 된다.
    # GET 방식의 요청이 들어오면 
    else:
        # ReservationForm을 context에 담아 create.html로 전달하여 render한다.
        form = ReservationForm()
    context = {
        'form': form,
    }
    return render(request, 'reservations/create.html', context)
    

def index(request):
    # Q2-2
    # Reservation 모델의 모든 데이터들을 id 기준 내림차순으로 받아온다.
    reservations = Reservation.objects.order_by('-id')
    # 데이터를 context에 담아 index.html로 전달하여 render한다.
    context = {
        'reservations': reservations,
    }
    return render(request, 'reservations/index.html', context)
    

def detail(request, pk):
    # Q2-3
    # pk값에 맞는 Reservation 데이터를 가져오는데 존재하지 않는다면 404페이지를 반환하기 위해 get_object_or_404를 사용한다.
    reservation = get_object_or_404(Reservation, pk=pk)
    comment_form = CommentForm()
    # 데이터를 가져왔다면 context에 담아 detail.html로 전달하여 render한다.
    context = {
        'reservation': reservation,
        'comment_form': comment_form,
    }
    return render(request, 'reservations/detail.html', context)
    

@require_POST
def comments_create(request, pk):
    # Q3-1
    # pk값에 맞는 Reservation 데이터를 가져오는데 존재하지 않는다면 404페이지를 반환하기 위해 get_object_or_404를 사용한다.
    reservation = get_object_or_404(Reservation, pk=pk)
    # CommentForm에 데이터를 받아
    comment_form = CommentForm(request.POST)
    # 데이터가 유효하다면
    if comment_form.is_valid():
        # ForeignKey인 reservation의 지정을 위한 임시 저장을 하기 위해 commit=False 사용
        comment = comment_form.save(commit=False)
        # reservation ForeginKey 설정
        comment.reservation = reservation
        # comment 저장
        comment.save()
        # 다시 detail 경로로 redirect
        return redirect('reservations:detail', pk)
    # 데이터가 유효하지 않다면 reservation 데이터와 오류 메시지를 담은 comment_form을 context에 담아 다시 render
    context = {
        'reservation': reservation,
        'comment_form': comment_form,
    }
    return render(request, 'reservations/detail.html', context)
