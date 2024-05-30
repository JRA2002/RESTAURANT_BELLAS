from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('account/', include('django.contrib.auth.urls')),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('menu/', views.MenuView.as_view(), name='menu'),
    path('menu/edit/', views.UpdateMenuView.as_view(), name='menu_edit'),
    path('menu/new/', views.CreateMenuView.as_view(), name='create_menu'),
    path('menu/<menu_item>', views.MenuDetailsView.as_view(), name='details'),
    path('menu/<menu_item>/edit/', views.UpdateMenuDetailsView.as_view(), name='menu_item_edit'),
    path('menu/<menu_item>/delete/', views.DeleteMenuView.as_view(), name='delete_menu'),
    path('menu/<menu_item>/edit/new/', views.CreateRecipeView.as_view(), name='create_recipe'),
    path('menu/<menu_item>/edit/description/', views.UpdateMenuDescriptionView.as_view(), name='update_description'),
    path('customerorders', views.TableOrderView.as_view(), name='table_order'),
    path('customerorders/new/', views.CreateTableOrderView.as_view(), name='create_table_order'),
    path('customerorders/<pk>/delete', views.DeleteTableOrderView.as_view(), name='delete_table_order'),
    path('customerorders/<pk>', views.PurchaseView.as_view(), name='purchases'),
    path('customerorders/<pk>/new/', views.CreatePurchaseView.as_view(), name='create_purchases'),
    path('customerorders/<order>/<menuitem>/update/', views.UpdatePurchaseView.as_view(), name='update_purchases'),
    path('customerorders/<order>/<menuitem>/delete/', views.DeletePurchaseView.as_view(), name='delete_purchases'),
    path('salesprofit/', views.SalesProfitView.as_view(), name='sales_profit'),
    path('salesprofit/reports/', views.ReportView.as_view(), name='report'),
    path('salesprofit/bestsellers', views.BestSellerView.as_view(), name='best_sellers'),
    path('stock/', views.StockView.as_view(), name='stock'),
    path('stock/currentstock/', views.CurrentStockView.as_view(), name='current_stock'),
    path('stock/currentstock/update/', views.UpdateStockView.as_view(), name='update_stock'),
    path('stock/stockedrecipes/', views.StockedRecipes.as_view(), name='stocked_recipes'),
    path('stock/shoppinglist/', views.ShoppingList.as_view(), name='shopping_list'),
    path('stock/shoppinglist/add/<ingredient>', views.CreateBasketView.as_view(), name='add_to_basket'),
    path('stock/shoppinglist/update/<ingredient>', views.UpdateBasketView.as_view(), name='update_basket'),
    path('stock/basket/', views.BasketView.as_view(), name='basket_view'),
    path('stock/basket/add', views.AddBasketView.as_view(), name='add_any'),
    path('stock/basket/edit', views.EditBasketView.as_view(), name='edit_basket'),
    path('stock/ingredients/', views.IngredientView.as_view(), name='ingredients'),
    path('stock/ingredients/new/', views.CreateIngredientView.as_view(), name='create_ingredients'),
    path('stock/ingredients/<name>/update/', views.UpdateIngredientView.as_view(), name='update_ingredients'),
    path('stock/ingredients/<name>/delete/', views.DeleteIngredientView.as_view(), name='delete_ingredients'),
    path('stock/ingredients/orphans/', views.OrphanIngredientView.as_view(), name='orphans'),
    path('stock/orders', views.OrderView.as_view(), name='orders'),
    path('stock/orders/add/', views.CreateOrderView.as_view(), name='create_order'),
]