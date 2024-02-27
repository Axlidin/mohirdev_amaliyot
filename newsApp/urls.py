from django.urls import path

from .views import (get_newsList, getnews_detail, Get_News_Detail_List, Get_News_List, HomePage_views,
                    contactViews, error_pages, about_me, HomePageView,
                    ErrorViews, AboutMeViews, ContactPageViews, LocalNewsView,
                    ForeignNewsView, SportNewsView, TechnologyNewsView)
urlpatterns = [
    path("", HomePageView.as_view(), name='home_page'),
    path("contact-me/", ContactPageViews.as_view(), name='contact'),
    path("error_pages/", ErrorViews.as_view(), name='error'),
    path("about-me/", AboutMeViews.as_view(), name='about_me'),
    path("news/", Get_News_List.as_view(), name="all_news_list"),
    path("local-news/", LocalNewsView.as_view(), name="local_news_page"),
    path("foreign-news/", ForeignNewsView.as_view(), name="foreign_news_page"),
    path("sport-news/", SportNewsView.as_view(), name="sport_news_page"),
    path("technology-news/", TechnologyNewsView.as_view(), name="technology_news_page"),
    path("news/<slug:news>/", getnews_detail, name="news_detail_page"),
]