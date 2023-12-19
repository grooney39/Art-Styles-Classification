from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from style_classification.pre_processing import execute_model_p1, execute_model_p2
import os

# imports for prediction

# Create your views here.

labels = {0: 'Ikona_bizantyjska',
          1: 'Renesans',
          2: 'Neorenesans',
          3: 'Wysoki_renesans',
          4: 'Barok',
          5: 'Rokoko',
          6: 'Romantyzm',
          7: 'Realizm',
          8: 'Impresjonizm',
          9: 'Postimpresjonizm',
          10: 'Ekspresjonizm',
          11: 'Symbolizm',
          12: 'Fowizm',
          13: 'Kubizm',
          14: 'Surrealizm',
          15: 'Abstrakcja',
          16: 'Prymitywizm',
          17: 'Pop_Art'}


def index(request):
    return render(request, 'index.html', context={'a': 1})

def methods(request):
    return render(request, 'methods.html', context={'a': 1})

def styles(request):
    return render(request, 'styles.html', context={'a': 1})

def about(request):
    return render(request, 'about.html', context={'a': 1})

def style1(request):
    path = "./media/new/"
    files = [f for f in os.listdir(path) if f.endswith("Ikona_bizantyjska")]
    urls = [os.path.join(path, f) for f in files]
    titles = [os.path.basename(f) for f in files]
    files_data = list(zip(urls, titles))
    return render(request, 'byzantin_iconography.html', context={'files': files_data})

def style2(request):
    path = "./media/new/"
    files = [f for f in os.listdir(path) if f.endswith("Renesans")]
    urls = [os.path.join(path, f) for f in files]
    titles = [os.path.basename(f) for f in files]
    files_data = list(zip(urls, titles))
    return render(request, 'early_renaissance.html', context={'files': files_data})

def style3(request):
    path = "./media/new/"
    files = [f for f in os.listdir(path) if f.endswith("Neorenesans")]
    urls = [os.path.join(path, f) for f in files]
    titles = [os.path.basename(f) for f in files]
    files_data = list(zip(urls, titles))
    return render(request, 'northern_renaissance.html', context={'files': files_data})

def style4(request):
    path = "./media/new/"
    files = [f for f in os.listdir(path) if f.endswith("Wysoki_renesans")]
    urls = [os.path.join(path, f) for f in files]
    titles = [os.path.basename(f) for f in files]
    files_data = list(zip(urls, titles))
    return render(request, 'high_renaissance.html', context={'files': files_data})

def style5(request):
    path = "./media/new/"
    files = [f for f in os.listdir(path) if f.endswith("Barok")]
    urls = [os.path.join(path, f) for f in files]
    titles = [os.path.basename(f) for f in files]
    files_data = list(zip(urls, titles))
    return render(request, 'baroque.html', context={'files': files_data})

def style6(request):
    path = "./media/new/"
    files = [f for f in os.listdir(path) if f.endswith("Rokoko")]
    urls = [os.path.join(path, f) for f in files]
    titles = [os.path.basename(f) for f in files]
    files_data = list(zip(urls, titles))
    return render(request, 'rococo.html', context={'files': files_data})

def style7(request):
    path = "./media/new/"
    files = [f for f in os.listdir(path) if f.endswith("Romantyzm")]
    urls = [os.path.join(path, f) for f in files]
    titles = [os.path.basename(f) for f in files]
    files_data = list(zip(urls, titles))
    return render(request, 'romantism.html', context={'files': files_data})

def style8(request):
    path = "./media/new/"
    files = [f for f in os.listdir(path) if f.endswith("Realizm")]
    urls = [os.path.join(path, f) for f in files]
    titles = [os.path.basename(f) for f in files]
    files_data = list(zip(urls, titles))
    return render(request, 'realism.html', context={'files': files_data})

def style9(request):
    path = "./media/new/"
    files = [f for f in os.listdir(path) if f.endswith("Impresionizm")]
    urls = [os.path.join(path, f) for f in files]
    titles = [os.path.basename(f) for f in files]
    files_data = list(zip(urls, titles))
    return render(request, 'impressionism.html', context={'files': files_data})

def style10(request):
    path = "./media/new/"
    files = [f for f in os.listdir(path) if f.endswith("Postimpresionizm")]
    urls = [os.path.join(path, f) for f in files]
    titles = [os.path.basename(f) for f in files]
    files_data = list(zip(urls, titles))
    return render(request, 'post_impressionism.html', context={'files': files_data})

def style11(request):
    path = "./media/new/"
    files = [f for f in os.listdir(path) if f.endswith("Ekspresionizm")]
    urls = [os.path.join(path, f) for f in files]
    titles = [os.path.basename(f) for f in files]
    files_data = list(zip(urls, titles))
    return render(request, 'expressionism.html', context={'files': files_data})

def style12(request):
    path = "./media/new/"
    files = [f for f in os.listdir(path) if f.endswith("Symbolizm")]
    urls = [os.path.join(path, f) for f in files]
    titles = [os.path.basename(f) for f in files]
    files_data = list(zip(urls, titles))
    return render(request, 'symbolism.html', context={'files': files_data})

def style13(request):
    path = "./media/new/"
    files = [f for f in os.listdir(path) if f.endswith("Fowizm")]
    urls = [os.path.join(path, f) for f in files]
    titles = [os.path.basename(f) for f in files]
    files_data = list(zip(urls, titles))
    return render(request, 'fauvism.html', context={'files': files_data})

def style14(request):
    path = "./media/new/"
    files = [f for f in os.listdir(path) if f.endswith("Kubizm")]
    urls = [os.path.join(path, f) for f in files]
    titles = [os.path.basename(f) for f in files]
    files_data = list(zip(urls, titles))
    return render(request, 'cubism.html', context={'files': files_data})

def style15(request):
    path = "./media/new/"
    files = [f for f in os.listdir(path) if f.endswith("Surrealizm")]
    urls = [os.path.join(path, f) for f in files]
    titles = [os.path.basename(f) for f in files]
    files_data = list(zip(urls, titles))
    return render(request, 'surrealism.html', context={'files': files_data})

def style16(request):
    path = "./media/new/"
    files = [f for f in os.listdir(path) if f.endswith("Abstrakcja")]
    urls = [os.path.join(path, f) for f in files]
    titles = [os.path.basename(f) for f in files]
    files_data = list(zip(urls, titles))
    return render(request, 'abstract_art.html', context={'files': files_data})

def style17(request):
    path = "./media/new/"
    files = [f for f in os.listdir(path) if f.endswith("Prymitywizm")]
    urls = [os.path.join(path, f) for f in files]
    titles = [os.path.basename(f) for f in files]
    files_data = list(zip(urls, titles))
    return render(request, 'naive_art.html', context={'files': files_data})

def style18(request):
    path = "./media/new/"
    files = [f for f in os.listdir(path) if f.endswith("Pop_Art")]
    urls = [os.path.join(path, f) for f in files]
    titles = [os.path.basename(f) for f in files]
    files_data = list(zip(urls, titles))
    return render(request, 'pop_art.html', context={'files': files_data})

def predictImage(request):
    fileObj = request.FILES['filePath']
    selectedModel = request.POST.get('models', '')
    filename = request.POST.get('fileName', '')
    fs = FileSystemStorage()
    filePathName = fs.save(filename, fileObj)
    filePathName = fs.url(filePathName)
    testimage = '.' + filePathName

    if selectedModel == 'model1':
        modelPath = './models/pt_p1_50e_v1.pth'
        print(testimage)
        predict, avg_pred, max_prob = execute_model_p1(modelPath, testimage)
    elif selectedModel == 'model2':
        modelPath = './models/pt_p2_50e_v1.pth'
        predict, avg_pred, max_prob = execute_model_p2(modelPath, testimage)
    elif selectedModel == 'model3':
        modelPath = './models/fs_p1_15e_v1.pth'
        predict, avg_pred, max_prob = execute_model_p1(modelPath, testimage)
    print(predict)
    print(avg_pred)
    print(max_prob)
    # predict = execute_model_p2(modelPath, testimage).item()
    predictedLabel = labels[predict]

    # Po uzyskaniu etykiety możesz wykonać operacje na pliku, np. przeniesienie do innego katalogu
    new_file_path = './media/new/' + filename + '_' + selectedModel + '_' + predictedLabel
    os.rename(testimage, new_file_path)
    predictedLabel = predictedLabel.replace('_', ' ')

    # Usunięcie pliku z poprzedniej ścieżki, jeśli nie jest już potrzebny
    # fs.delete(filePathName)

    context = {'filePathName': new_file_path, 'filename': filename, 'predictedLabel': predictedLabel, 'prob':max_prob}
    return render(request, 'index.html', context=context)

