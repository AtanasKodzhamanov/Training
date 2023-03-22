using CarRacing.Models.Cars.Contracts;
using CarRacing.Utilities.Messages;
using System;
using System.Collections.Generic;
using System.Text;

namespace CarRacing.Models.Cars
{
    public abstract class Car : ICar
    {
        private string make;
        private string model;
        private string vin;
        private int horsepower;
        private double fuelavailable;
        private double fuelcons;

        public string Make
        {
            get
            {
                return this.make;
            }
            private set
            {
                if (string.IsNullOrWhiteSpace(value))
                {
                    throw new ArgumentException(ExceptionMessages.InvalidCarMake);
                }
                this.make = value;
            }
        }
        public string Model
        {
            get
            {
                return this.model;
            }
            private set
            {
                if (string.IsNullOrWhiteSpace(value))
                {
                    throw new ArgumentException(ExceptionMessages.InvalidCarModel);
                }
                this.model = value;
            }
        }
        public string VIN
        {
            get
            {
                return this.vin;
            }
            private set
            {
                if (value.Length !=17)
                {
                    throw new ArgumentException(ExceptionMessages.InvalidCarVIN);
                }
                this.vin = value;
            }
        }
        public int HorsePower
        {
            get
            {
                return this.horsepower;
            }
            protected set
            {
                if (value<0)
                {
                    throw new ArgumentException(ExceptionMessages.InvalidCarHorsePower);
                }
                this.horsepower = value;
            }
        }
        public double FuelAvailable
        {
            get
            {
                return this.fuelavailable;
            }
            private set
            {
                if (value < 0)
                {
                    throw new ArgumentException(ExceptionMessages.InvalidCarFuelConsumption);
                }
                this.fuelavailable = value;
            }
        }
        public double FuelConsumptionPerRace
        {
            get
            {
                return this.fuelcons;
            }
            private set
            {
                if (value < 0)
                {
                    this.fuelcons = 0;
                }
                this.fuelcons = value;
            }
        }

          protected Car(string make, string model, string vin, int horsepower, double fuelavailable, double fuelcons)
        {
            this.Make = make;
            this.Model = model;
            this.VIN = vin;
            this.HorsePower = horsepower;
            this.FuelAvailable = fuelavailable;
            this.FuelConsumptionPerRace = fuelcons;
        }
        public virtual void Drive()
        {
         
            FuelAvailable -= FuelConsumptionPerRace;

            //pod nula?
           
            //More stuff
        }
    }
}
