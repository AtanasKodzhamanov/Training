using CarRacing.Models.Cars.Contracts;
using CarRacing.Repositories.Contracts;
using System;
using CarRacing.Utilities.Messages;

using System.Collections.Generic;
using System.Text;
using System.Linq;

namespace CarRacing.Repositories
{
    public class CarRepository : IRepository<ICar>
    {
        private readonly List<ICar> cars;
        public IReadOnlyCollection<ICar> Models => this.cars.AsReadOnly();

        public void Add(ICar car)
        {
            if(car == null)
            {
                throw new ArgumentException(ExceptionMessages.InvalidAddCarRepository);
            }
            this.cars.Add(car); //Does it return success?
        }

        public ICar FindBy(string property) => this.cars.FirstOrDefault(x => x.VIN == property);
       

        public bool Remove(ICar car) => this.cars.Remove(car); //Does it return success?
      
    }


}
