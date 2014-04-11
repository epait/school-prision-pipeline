from county_info.models import District, Graduation, DisciplineRate, Demographics, Attendance, GradeLevel, SpecialCourses, FreeLunch, State, StateDemographics, StateGraduation, StateAttendance, StateGradeLevel, StateSpecialCourses, StateDiscipline
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def home(request):
	northcarolina = State.objects.get(state_name="North Carolina")
	context = {
		'northcarolina': northcarolina,
		'districts': District.objects.all(),
	}
	# ipdb.set_trace()

	# district_input = "Orange County Schools"
	# school_year_input = "2012-2013"
	# district = District.objects.get(lea_name=district_input)
	# graduation_rates = district.graduation_rates.get(school_year=school_year_input)
	# black_graduation_rate = graduation_rates.black_graduation_rate
	
	return render(request, "county_info/home.html", context)

def mobile(request):
	context = {
	}
	return render(request, "county_info/mobile.html", context)