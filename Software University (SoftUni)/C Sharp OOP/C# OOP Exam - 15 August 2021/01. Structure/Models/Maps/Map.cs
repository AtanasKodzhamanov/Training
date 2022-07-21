using CarRacing.Models.Maps.Contracts;
using CarRacing.Models.Racers.Contracts;
using System;
using System.Collections.Generic;
using System.Text;

namespace CarRacing.Models.Maps
{
    public class Map : IMap
    {
        public string StartRace(IRacer racerOne, IRacer racerTwo)
        {
            if (racerOne.IsAvailable() && racerTwo.IsAvailable())
            {
                racerOne.Race();
                racerTwo.Race();
                double mult1;
                double mult2;

                if (racerOne.RacingBehavior == "Aggressive")
                {
                    mult1 = 1.1;
                }
                else { mult1 = 1.2; }

                if (racerTwo.RacingBehavior == "Aggressive")
                {
                    mult2 = 1.1;
                }
                else { mult2 = 1.2; }

                double winchance1 = racerOne.Car.HorsePower * racerOne.DrivingExperience * mult1;
                double winchance2 = racerTwo.Car.HorsePower * racerTwo.DrivingExperience * mult2;

                if (winchance1 > winchance2)
                {
                    return $"{racerOne.Username} has just raced against {racerTwo.Username}! {racerOne.Username} is the winner!";
                }
                else
                {
                    return $"{racerOne.Username} has just raced against {racerTwo.Username}! {racerTwo.Username} is the winner!";

                }
            }
            else if(!racerOne.IsAvailable() && racerTwo.IsAvailable())
            {
                return $"{racerTwo.Username} wins the race! {racerOne.Username} was not available to race!";
            }
            else if (racerOne.IsAvailable() && !racerTwo.IsAvailable())
            {
                return $"{racerOne.Username} wins the race! {racerTwo.Username} was not available to race!";
            }
            else 
            {
                return $"Race cannot be completed because both racers are not available!";
            }
        }
    }
}
