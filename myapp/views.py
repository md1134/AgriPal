from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Farm, EnvironmentalData, Crop, Prediction, Recommendation
from .forms import EnvironmentalForm
from ml.predictor import predict_crop  # AI module


def home(request):
    farms = Farm.objects.all()
    return render(request, 'myapp/home.html', {'farms': farms})


def farm_env_data(request, farm_id):
    farm = get_object_or_404(Farm, id=farm_id)


    if request.method == "POST":
        form = EnvironmentalForm(request.POST)
        if form.is_valid():
            env_data = form.save(commit=False)
            env_data.farm = farm
            env_data.save()


            # AI prediction
            data_dict = form.cleaned_data
            crop_name = predict_crop(data_dict)
            crop = Crop.objects.get(name=crop_name)


            prediction = Prediction.objects.create(
                farm=farm,
                crop=crop,
                confidence=85.0  # placeholder
            )


            recommendation = Recommendation.objects.create(
                prediction=prediction,
                planting_month="Nov–Dec",
                fertilizer_plan="Apply 50kg N/ha",
                irrigation_plan="Irrigate every 5 days",
                pest_warning="Watch out for pests"
            )


            return render(request, 'myapp/result.html', {
                'prediction': prediction,
                'recommendation': recommendation
            })
    else:
        form = EnvironmentalForm()


    return render(request, 'myapp/farm_form.html', {'form': form, 'farm': farm})
