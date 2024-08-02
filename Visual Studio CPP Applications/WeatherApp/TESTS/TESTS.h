#pragma once
#include "LocationManager.h"
#include "WeatherAPI.h"
#include "WeatherForecast.h"


class Tests
{
	public:
		Tests(WeatherAPIAccess api, WeatherManagement forecast, LocationManagement &locationManagement);
		void TestAdd();
		void TestModify();
		void TestDelete();
		void TestFavourite();
	
	private:
		WeatherAPIAccess t_API;
		WeatherManagement t_Forecast;
		LocationManagement t_LocManager;
};