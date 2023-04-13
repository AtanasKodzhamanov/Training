﻿using System;
using System.Collections.Generic;
using System.Text;

namespace CarRacing.Models.Cars
{
    public class TunedCar : Car
    {
        public TunedCar(string make, string model, string vin, int horsepower) : base(make, model, vin, horsepower, 65, 7.5)
        {
        }

        public override void  Drive()
        {
            base.Drive();
            HorsePower = (int)Math.Round(HorsePower * 0.97);
        }
    }
}