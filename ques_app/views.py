from django.shortcuts import render,redirect
from .models import Question_Details,Answer_Details
import random
from .ML import Idator
# Create your views here.
#TO DO'S
#incorporate the ML part with this
def QuesterTrainView(request):
    print(request.POST)
    auth=auth=request.POST.get('auth')
    flag=0
    if auth=='1' or request.session['auth']==1:
        request.session['auth']=1
        try:
            request.session['exam']=0
        except:
            request.session['exam']=0
        request.session['train']=1
##        try:
##            request.session['correct_ans']
##        except:
##            request.session['correct_ans']=[]
##        try:
##            request.session['given_ans']
##        except:
##            request.session['given_ans']=[]
##        try:
##            request.session['no_correct_ans']
##        except:
##            request.session['no_correct_ans']='0'
        ques_list=request.session['ques_list']
        print("Train View")
        #print("Before question list",ques_list)
        if request.session['flag_qchange']:
            request.session['counter']=request.session['counter']-1 
        print("Counter",request.session['counter'])
        if request.session['counter']==20:
            ques_list=[]
            request.session['ques_list']=ques_list
            #Answer=Answer_Details(ans_right=request.session['no_correct_ans'],avg_time=str((((int(request.session['stu_time'])/20)/60)/60)),avg_clicks=str(int(request.session['stu_clicks'])/20),avg_marked=str(request.session['mark_review']))
            #Answer.save()
            return MLView(request)

        #question_no=random.choice([i for i in range(1,41) if i not in ques_list])
        question_no=request.session['ques_list'][request.session['counter']]
        print("FLAG",request.session['flag_qchange'])
        request.session['counter']=request.session['counter']+1            
        question=Question_Details.objects.filter(id=question_no)
        print("question_no",question_no)
        ques_list.append(question_no)
        request.session['ques_list']=ques_list
        print("question list",ques_list)
        if not request.session['flag_qchange']:
            temp_ans=request.session['correct_ans']
            temp_ans.append(question.values('correct_ans')[0]['correct_ans'])
            request.session['correct_ans']=temp_ans

        if request.session['flag_qchange']:
            request.session['flag_qchange']=0

        return render(request, 'page.html',
                      {"ques_item":question,"counter":range(int(request.session['counter'])-1),"ques_no":int(request.session['counter'])})
    return redirect('/main/')

def QuesterExamView(request):
    print(request.POST)
    auth=request.POST.get('auth')
    flag=0
    if auth=='1' or request.session['auth']==1:
        request.session['auth']=1
        try:
            request.session['train']=0
        except:
            request.session['train']=0
        request.session['exam']=1
##        try:
##            request.session['ques_list']
##        except:
##            request.session['ques_list']=[]
##        try:
##            request.session['no_correct_ans']
##        except:
##            request.session['no_correct_ans']='0'
        ques_list=request.session['ques_list']
        print("Exam View")
        #print("before question list",ques_list)
        if request.session['flag_qchange']:
            request.session['counter']=request.session['counter']-1
        print("Counter",request.session['counter'])
        if request.session['counter']==20:
            ques_list=[]
            request.session['ques_list']=ques_list
            return MLView(request)
            
        question_no=request.session['ques_list'][request.session['counter']]
        print("FLAG",request.session['flag_qchange'])
        request.session['counter']=request.session['counter']+1
        question=Question_Details.objects.filter(id=question_no)
        print("question_no",question_no)
        ques_list.append(question_no)
        request.session['ques_list']=ques_list
        print("question list",ques_list)
        if not request.session['flag_qchange']:
            temp_ans=request.session['correct_ans']
            temp_ans.append(question.values('correct_ans')[0]['correct_ans'])
            request.session['correct_ans']=temp_ans

        if request.session['flag_qchange']:
            request.session['flag_qchange']=0

        return render(request, 'page.html',
                      {"ques_item":question,"counter":range(int(request.session['counter'])-1),"ques_no":int(request.session['counter']),"ans_list":request.session['given_ans']})
    return redirect('/main/')    
        
#incorporate exam finished part
def ValidatorView(request):
    print(request.POST)
    if request.session['auth']==1:
        exam_finished=request.POST.get('exam_finished')
        if exam_finished=='1':
            stu_clicks=request.POST.get('stu_clicks')
            stu_time=request.POST.get('stu_time')
            request.session['stu_clicks']=str(int(request.session['stu_clicks'])+int(stu_clicks))
            request.session['stu_time']=str(int(request.session['stu_time'])+int(stu_time))
            ans=request.POST.get('ans')
            if not ans:
                ans='0'

            temp_ans=request.session['given_ans']
            temp_ans.append(ans)
            request.session['given_ans']=temp_ans
            c_ans=request.session['correct_ans']
            given_temp=request.session['given_ans']
            print("Given Answer",given_temp)
            print("Correct Answer List",c_ans)
            print("Comming here")
            for i in range(len(c_ans)):
                if not given_temp:
                    request.session['no_correct_ans']=0
                    break
                if given_temp[i]==c_ans[i]:
                    request.session['no_correct_ans']=str(int(request.session['no_correct_ans'])+1)
                    print("request.session ans",request.session['no_correct_ans'])
            temp=[]
            request.session['given_ans']=temp
            request.session['correct_ans']=temp
            return MLView(request)
            
        ques_index=request.POST.get('ques_no')
        print("question index",ques_index)
        if ques_index:
            question=Question_Details.objects.filter(id=request.session['ques_list'][int(ques_index)])
            request.session['flag_qchange']=1
            request.session['ques_index']=ques_index
            stu_clicks=request.POST.get('stu_clicks')
            stu_time=request.POST.get('stu_time')
            request.session['stu_clicks']=str(int(request.session['stu_clicks'])+int(stu_clicks))
            request.session['stu_time']=str(int(request.session['stu_time'])+int(stu_time))

            return render(request, 'page.html',{"ques_item":question,"counter":range(int(request.session['counter'])-1),"ques_no":int(request.session['counter']),"ans_list":request.session['given_ans'],"ans_list":request.session['given_ans']})
            
            
        #print("session auth",request.session['auth'])
        ans=request.POST.get('ans')
        if not ans:
            ans='0'
        if request.session['flag_qchange']:
            temp_ans=request.session['given_ans']
            temp_ans[int(request.session['ques_index'])]=ans
            request.session['given_ans']=temp_ans
            #request.session['flag_qchange']=0
        else:   
            temp_ans=request.session['given_ans']
            temp_ans.append(ans)
            request.session['given_ans']=temp_ans

        stu_clicks=request.POST.get('stu_clicks')
        stu_time=request.POST.get('stu_time')
        mark_review=request.POST.get('mark_review')
        try:
            request.session['stu_clicks']=str(int(request.session['stu_clicks'])+int(stu_clicks))
        except:
            request.session['stu_clicks']='0'
        try:
            request.session['stu_time']=str(int(request.session['stu_time'])+int(stu_time))
        except:
            request.session['stu_time']='0'
        try:
            request.session['mark_review']=str(int(request.session['mark_review'])+int(mark_review))
        except:
            request.session['mark_review']='0'


        c_ans=request.session['correct_ans']
        print("Given Answer",request.session['given_ans'])
        print("Correct Answer List",c_ans)
        print("Clicks",request.session['stu_clicks'])
        print("Time",request.session['stu_time'])
        print("Marked For Reviews",request.session['mark_review'])
        if len(request.session['given_ans'])==20:
            given_temp=request.session['given_ans']
            print("Comming here")
            for i in range(len(c_ans)):
                if given_temp[i]==c_ans[i]:
                    request.session['no_correct_ans']=str(int(request.session['no_correct_ans'])+1)
                    print("request.session ans",request.session['no_correct_ans'])
            temp=[]
            request.session['given_ans']=temp
            request.session['correct_ans']=temp
        if request.session['train']:
            return QuesterTrainView(request)
        if request.session['exam']:
            return QuesterExamView(request)

    return redirect('/main/')
    
def MLView(request):
    data=[]
    data.extend([[str((((int(request.session['stu_time'])/1000)/60)/20)),str(request.session['mark_review']),request.session['no_correct_ans'],str(int(request.session['stu_clicks'])/20)]])
    print("ML data from website",data)
    data=[['2.5','5','17','2.25']]
    answer=Answer_Details.objects.all().values()
    predict_data=Idator(answer,data)
    predict_data['right']=request.session['no_correct_ans']
    print(predict_data)
    #Answer=Answer_Details(ans_right=request.session['no_correct_ans'],avg_time=str((((int(request.session['stu_time'])/1000)/60)/20)),avg_clicks=str(int(request.session['stu_clicks'])/20),avg_marked=str(request.session['mark_review']),stu_class=predict_data['dtree'])
    #Answer.save()
    request.session['no_correct_ans']=0
    request.session['stu_time']=0
    request.session['stu_clicks']=0
    request.session['mark_review']=0
    print("Next user taking test")
    lst = list(range(1,41))
    ques_list=random.sample(lst, 20)
    request.session['ques_list']=ques_list
    request.session['counter']=0
    if request.session['exam']:
        return render(request, 'exam.html',{"predict_item":predict_data})
    if request.session['train']:
        return render(request, 'train.html')

def MainView(request):
    #print(request.POST)
    #auth=request.POST.get('auth')
    ques_list=[]
    request.session['auth']=0
    request.session['ques_list']=ques_list
    request.session['correct_ans']=ques_list
    request.session['given_ans']=ques_list
    request.session['no_correct_ans']=0
    request.session['stu_time']=0
    request.session['stu_clicks']=0
    request.session['mark_review']=0
    request.session['flag_qchange']=0
    lst = list(range(1,41))
    ques_list=random.sample(lst, 20)
    request.session['ques_list']=ques_list
    request.session['counter']=0
    return render(request, 'main.html')
    
