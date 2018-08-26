from django.http import HttpResponse
from django.views.generic import View
from django.template import loader

from webrecruiter.utils import render_to_pdf #created in step 4
# from jobapply.models import Candidate_Basic

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        # all_candidate = Candidate_Basic.object.all()
        # print(all_candidate)
        template = loader.get_template('invoice.html')
        context = {
            'invoice_id': 123,
            'customer_name': 'John Cooper',
            'amount': 139.99,
            'today' : "Today",
        }
        html = template.render(context)
        pdf = render_to_pdf('invoice.html',context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("1234")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")
