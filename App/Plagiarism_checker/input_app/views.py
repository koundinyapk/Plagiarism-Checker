from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse,FileResponse

def home(request):
    return render(request,'index.html')

# Create your views here.

#from google.colab import files
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def vectorize(Text): 
    return TfidfVectorizer().fit_transform(Text).toarray()

def similarity(doc1, doc2): 
    return cosine_similarity([doc1, doc2])

def check_plagiarism(request):
    if request.method == 'POST':
        # Get the uploaded files from the request
        uploaded_files = request.FILES.getlist('input_files')
        student_notes = []

        # Process each uploaded file
        for uploaded_file in uploaded_files:
            # Read the content of the file and decode it
            file_content = uploaded_file.read().decode('utf-8').strip()
            student_notes.append(file_content)

        # Perform plagiarism check using the student notes
        plagiarism_results = set()
        vectors = vectorize(student_notes)
        s_vectors = list(zip(range(1, len(student_notes) + 1), vectors))
        
        for student_a, text_vector_a in s_vectors:
            new_vectors = s_vectors.copy()
            current_index = new_vectors.index((student_a, text_vector_a))
            del new_vectors[current_index]
            
            if(current_index==0):
                for student_b, text_vector_b in new_vectors:
                    sim_score = similarity(text_vector_a, text_vector_b)[0][1]
                    student_pair = sorted((student_a, student_b))
                    score = (student_pair[0], student_pair[1], sim_score)
                    plagiarism_results.add(score)
        
        # Render the results.html template with plagiarism results as context data
        return render(request, 'result.html', {'plagiarism_results': plagiarism_results})
    else:
        # Handle other request methods (GET, etc.)
        return HttpResponse("Method not allowed")


'''from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def vectorize(Text): 
    return TfidfVectorizer().fit_transform(Text).toarray()

def similarity(doc1, doc2): 
    return cosine_similarity([doc1, doc2])

def check_plagiarism(request):
    if request.method == 'POST':
        # Get the uploaded files from the request
        uploaded_files = request.FILES.getlist('input_files')
        student_notes = []

        # Process each uploaded file
        for uploaded_file in uploaded_files:
            # Read the content of the file and decode it
            file_content = uploaded_file.read().decode('utf-8').strip()
            student_notes.append(file_content)

        # Perform plagiarism check using the student notes
        plagiarism_results = []
        vectors = vectorize(student_notes)
        s_vectors = list(zip(range(1, len(student_notes) + 1), vectors))
        
        for student_a, text_vector_a in s_vectors:
            new_vectors = s_vectors.copy()
            current_index = new_vectors.index((student_a, text_vector_a))
            del new_vectors[current_index]
            
            if current_index == 0:
                for student_b, text_vector_b in new_vectors:
                    sim_score = similarity(text_vector_a, text_vector_b)[0][1]
                    student_pair = sorted((student_a, student_b))
                    score = (student_pair[0], student_pair[1], sim_score)
                    plagiarism_results.append(score)
        
        # Prepare data for rendering
        data_to_render = []
        for data in plagiarism_results:
            # Determine image URL based on plagiarism score
            if data[2] > 0.15:
                img_url = 'red'
            else:
                img_url = 'green'
            data_to_render.append((data[0], data[1], img_url))
        
        # Render the result.html template with plagiarism results and image URLs
        return render(request, 'result.html', {'plagiarism_results': data_to_render})
    else:
        # Handle other request methods (GET, etc.)
        return HttpResponse("Method not allowed")'''




