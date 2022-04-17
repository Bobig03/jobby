from django.shortcuts import get_object_or_404, render

from .models import JobPosting, Company, Category


def job_posting_list(request):
    job_postings = JobPosting.objects.order_by("-created_at").all()
    context = {"job_postings": job_postings}

    return render(request, "job_postings/list.html", context)


def job_posting_detail(request, id):
    job_posting = get_object_or_404(JobPosting, pk=id)
    context = {"job_posting": job_posting}

    return render(request, "job_postings/detail.html", context)


def company_list(request):
    companies = Company.objects.order_by("-created_at").all()
    context = {"companies": companies}

    return render(request, "companies/list.html", context)


def company_detail(request, id):
    company = get_object_or_404(Company, pk=id)
    job_postings = company.postings.all()
    context = {"company": company, "company_postings": job_postings}

    return render(request, "companies/detail.html", context)


def category_list(request):
    categories = Category.objects.order_by("name").all()
    context = {"categories": categories}
    return render(request, "categories/list.html", context)


def category_detail(request, id):
    category = get_object_or_404(Category, pk=id)
    job_postings = category.postings.all()
    context = {"category": category, "category_postings": job_postings}
    
    return render(request, "categories/detail.html", context)
