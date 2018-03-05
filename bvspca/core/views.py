from django.conf import settings
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from wagtail.core.models import Page
from wagtail.search.models import Query


def site_search(request):
    search_query = request.GET.get('query', None)
    page = request.GET.get('page', request.GET.get('p', 1))
    results_per_page = settings.SPCA_LIST_PAGE_LENGTH
    if search_query:
        search_results = Page.objects.live().search(search_query)
        Query.get(search_query).add_hit()
    else:
        search_query = ''
        search_results = Page.objects.none()
    paginator = Paginator(search_results, results_per_page)
    try:
        search_results = paginator.page(page)
    except PageNotAnInteger:
        search_results = paginator.page(1)
    except EmptyPage:
        search_results = paginator.page(paginator.num_pages)

    return render(request, 'core/search_results.html', {
        'search_query': search_query,
        'search_results': search_results,
        'title': '{} Search Results for: {}'.format(settings.SPCA_SITE_SHORT_NAME, search_query),
    })
