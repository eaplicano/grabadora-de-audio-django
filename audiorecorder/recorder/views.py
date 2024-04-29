from django.shortcuts import render, redirect
from .forms import AudioRecordingForm
from .models import AudioRecording

def home(request):
    form = AudioRecordingForm()
    recordings = AudioRecording.objects.all()
    return render(request, 'recorder/home.html', {'form': form, 'recordings': recordings})

def save_audio(request):
    if request.method == 'POST':
        print(request.POST['audio_file'])
        print(request.FILES)
        form = AudioRecordingForm(request.POST, request.FILES)
        
        if form.is_valid():
            print("Es valido")
            form.save(commit=True)
            return redirect('test')
        else:
            print("Es invalido")
    return redirect('home')

def test(request):
    
    return render(request, 'recorder/test.html')