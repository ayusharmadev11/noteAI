from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializer
import llama
import gpt


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all().order_by('-created_at')
    serializer_class = NoteSerializer

    def get_model_func(self, model_name, function_name):
        if model_name == "gpt":
            return getattr(gpt, function_name, None)
        elif model_name == "llama":
            return getattr(llama, function_name, None)
        else:
            return getattr(llama, function_name, None)


    @action(detail=False, methods=['post'])
    def rewrite(self, request):
        input_text = request.data.get("text", "")
        model = request.data.get("model", "gpt")

        func = self.get_model_func(model, "rewrite_text")
        if not func:
            return Response({"error": "Invalid model"}, status=status.HTTP_400_BAD_REQUEST)

        result = func(input_text)
        return Response({"result": result})


    @action(detail=False, methods=['post'])
    def summarize(self, request):
        input_text = request.data.get("text", "")
        model = request.data.get("model", "gpt")

        func = self.get_model_func(model, "summarize_text")
        if not func:
            return Response({"error": "Invalid model"}, status=status.HTTP_400_BAD_REQUEST)

        result = func(input_text)
        return Response({"result": result})


    @action(detail=False, methods=['post'])
    def generate_idea(self, request):
        model = request.data.get("model", "gpt")

        func = self.get_model_func(model, "generate_random_idea")
        if not func:
            return Response({"error": "Invalid model"}, status=status.HTTP_400_BAD_REQUEST)

        result = func()
        return Response({"result": result})

