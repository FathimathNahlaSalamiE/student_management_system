from django.shortcuts import render,redirect
from app.models import Student,Student_Notification,Student_Feedback
from django.contrib import messages

def HOME(request):
    return render(request,'Student/home.html')

def NOTIFICATIONS(request):
    student=Student.objects.filter(admin=request.user.id)
    for i in student:
        student_id=i.id
        notification=Student_Notification.objects.filter(student_id=student_id)
        context={
            'notification':notification,
        }
        return render(request,'Student/notification.html',context)

def STUDENT_NOTIFICATION_MARK_AS_DONE(request,status):
    notification=Student_Notification.objects.get(id=status)
    notification.status=1
    notification.save()
    return redirect('student_notifications')

def STUDENT_FEEDBACK(request):
    student_id=Student.objects.get(admin=request.user.id)

    feedback_history=Student_Feedback.objects.filter(student_id=student_id)

    context={
        'feedback_history':feedback_history,
    }

    return render(request,'Student/feedback.html',context)

def STUDENT_FEEDBACK_SAVE(request):
    if request.method=="POST":
        feedback=request.POST.get('feedback')

        student=Student.objects.get(admin=request.user.id)

        feedback=Student_Feedback(
            student_id=student,
            feedback=feedback,
            feedback_reply="",
        )
        feedback.save()
        messages.success(request,'Feedback send successfully !')
        return redirect('student_feedback')