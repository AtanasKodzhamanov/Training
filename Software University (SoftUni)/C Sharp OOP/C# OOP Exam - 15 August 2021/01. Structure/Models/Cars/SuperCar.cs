using System;
using System.Collections.Generic;
using System.Text;

namespace CarRacing.Models.Cars
{
    public class SuperCar : Car
    {
        public SuperCar(string make, string model, string vin, int horsepower) : base(make, model, vin, horsepower, 80, 10)
        {
        }
    }
}
