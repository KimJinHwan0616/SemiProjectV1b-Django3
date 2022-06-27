from django.db.models import F
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_control

from board.models import Board

# 게시판 목록보기 처리
from member.models import Member

@cache_control(no_cache=True, no_store=True, must_revalidate=True)
def list(request):
    # select 'id', 'title', 'userid', 'regdate', 'views'
    # from borad order by id desc

    # bdlist = Board.objects.values(
    #         'id', 'title', 'userid', 'regdate', 'views')\
    #         .order_by('-id')

    # Board와 Member 테이블은 userid <-> id 컬럼을 기준으로 inner join을 실행
    bdlist = Board.objects.select_related('board')

    # join된 member 테이블의 userid 확인
    # bdlist.get(0).member.userid

    context = {'bds': bdlist}
    return render(request, 'board/list.html')

# 게시판 본문보기 처리
@cache_control(no_cache=True, no_store=True, must_revalidate=True)
def view(request):
    if request.get == 'GET':

    form = request.GET.dict()
    # print(form['bno'])

    # 본문글에 대한 조회수 증가
    # update board set views = views + 1
    # where id = ???

    # 이해
    # b = Board.objects.get(id=form['bno'])
    # b.views = b.views + 1
    # b.save()

    # 실전
    Board.objects.filter(id=form['bno'])\
        .update(views=F('views') + 1)


    # 본문글 조회
    # select * from board inner join member
    # where id = ???
    bd = Board.objects.select_related('member')\
        .get(id=form['bno'])

    elif request.method == 'POST':
        pass

    return render(request, 'board/view.html')

def write(request):

    return render(request, 'board/write.html')

# 본문글 삭제하기
# /remove?bno=***
def remove(request):
    if request.method == 'GET':
        form = request.GET.dict()

        # delete from board where bno = ??
        Board.objects.filter(id=form['bno']).delete()

    return redirect('/list')


def modify(request):
    if request.method == 'GET':
        form = request.GET.dict()

        # select * from board where bno = ???
        Board.objects.get(id=form['bno'])


    elif request.method == 'POST':
        form = request.POST.dict()

        # update board set title = ???, contents = ???
        # where bno = ???

        # 이해
        # b = Board.objects.get(id=form['bno'])
        # b.title = form['title']
        # b.contents = form['contents']
        # b.save()

        # 실전
        Board.objects.filter(id=form['bno'])\
              .update(title=form['title'], contents=form['contents'])

        # 본문글 수정완료시 view 페이지로 이동
        redirect('/view?bno=' + form['bno'])

    context = {'bd': bd}
    return render(request, 'board/modify.html', context)
