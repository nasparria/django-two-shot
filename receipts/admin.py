from django.contrib import admin

from receipts.models import ExpenseCategory, Account, Receipt

# Register your models here.


class ExpenseCategoryAdmin(admin.ModelAdmin):
    pass


class AccountAdmin(admin.ModelAdmin):
    pass


class ReceiptAdmin(admin.ModelAdmin):
    pass


admin.site.register(ExpenseCategory, ExpenseCategoryAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(Receipt, ReceiptAdmin)
