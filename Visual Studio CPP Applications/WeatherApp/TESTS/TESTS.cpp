#include "TESTS.h"


Tests::Tests(WeatherAPIAccess api, WeatherManagement forecast, LocationManagement &locationManagement)
{
	t_API = api;
	t_Forecast = forecast;
	t_LocManager = locationManagement;
	std::cout << "-----BEGIN TEST-----" << std::endl;
	std::cout << "\n";

	TestAdd();
}


void Tests::TestAdd()
{
	std::string temp;
	char http[400];

	sprintf_s(http, 400, "http://api.openweathermap.org/geo/1.0/direct?q=%s,%s&limit=5&appid=57046f60541764553fef9c90486bbf91", "New_York", "USA");
	t_API.MakeGeoRequest(http);

	*http = NULL;
	std::cout << "Would you like to add this location? (Y/N)";
	std::cin >> temp;
	sprintf_s(http, 400, "api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&appid=57046f60541764553fef9c90486bbf91&units=imperial", t_API.GetLatFromGeo().c_str(), t_API.GetLonFromGeo().c_str());
	t_Forecast.MakeForecastRequest(http);


	if (temp == "y" || temp == "Y") t_LocManager.AddLocation(t_Forecast.GetParsedObject()); t_Forecast.DisplayWeatherForecast(); std::cout << std::endl << "\n";
	TestModify();
}


void Tests::TestModify()
{
	std::cout << "MODIFY LOCATION" << std::endl;
	std::cout << "Modifying name" << std::endl;

	t_LocManager.ModifyLocation("Dover Beaches North", "name", "New York");
	TestFavourite();
}


void Tests::TestDelete()
{
	std::cout << "DELETE LOCATION" << std::endl;
	std::cout << "\n";

	t_LocManager.DeleteLocation("New York");

	std::cout << "-----TEST PASSED-----";
	std::cout << "\n";
}


void Tests::TestFavourite()
{
	std::cout << "ADD FAVOURITE LOCATION" << std::endl;
	std::cout << "\n";

	t_LocManager.SetFavouriteLocations("New York");
	TestDelete();
}