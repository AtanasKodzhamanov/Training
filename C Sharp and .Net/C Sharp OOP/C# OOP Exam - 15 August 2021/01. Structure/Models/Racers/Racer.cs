using CarRacing.Models.Cars.Contracts;
using CarRacing.Models.Racers.Contracts;
using CarRacing.Utilities.Messages;
using System;
using System.Collections.Generic;
using System.Text;

namespace CarRacing.Models.Racers
{
   public abstract class Racer : IRacer
    {
        private string username;
        private string racingbehavior;
        private int drivingexperience;
        private ICar car;

        protected Racer(string username, string racingbehavior, int drivingexperience, ICar car)
        {
            this.Username = username;
            this.RacingBehavior = racingbehavior;
            this.DrivingExperience = drivingexperience;
            this.Car = car;
        }

        public string Username
        {
            get
            {
                return this.username;
            }
            private set
            {
                if (string.IsNullOrWhiteSpace(value))
                {
                    throw new ArgumentException(ExceptionMessages.InvalidRacerName);
                }
                this.username = value;
            }
        }

        public string RacingBehavior
        {
            get
            {
                return this.racingbehavior;
            }
            private set
            {
                if (string.IsNullOrWhiteSpace(value))
                {
                    throw new ArgumentException(ExceptionMessages.InvalidRacerBehavior);
                }
                this.racingbehavior = value;
            }
        }
        public int DrivingExperience
        {
            get
            {
                return this.drivingexperience;
            }
            protected set
            {
                if (drivingexperience<0 || drivingexperience>100)
                {
                    throw new ArgumentException(ExceptionMessages.InvalidRacerDrivingExperience);
                }
                this.drivingexperience = value;
            }
        }

        public ICar Car
        {
            get
            {
                return this.car;
            }
            private set
            {
                if (car==null)
                {
                    throw new ArgumentException(ExceptionMessages.InvalidRacerCar);
                }
                this.car = value;
            }
        }

        public bool IsAvailable()
        {
            if (Car.FuelAvailable > 0)
            {
                return true;
            }
            else return false;
        }

        public virtual void Race()
        {
            car.Drive();
            
        }
    }
}
