using CarRacing.Models.Racers.Contracts;
using CarRacing.Repositories.Contracts;
using CarRacing.Utilities.Messages;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace CarRacing.Repositories
{
    public class RacerRepository : IRepository<IRacer>
    {
        private readonly List<IRacer> racers;
        public IReadOnlyCollection<IRacer> Models => this.racers.AsReadOnly();

        public void Add(IRacer racer)
        {
            if (racer == null)
            {
                throw new ArgumentException(ExceptionMessages.InvalidAddRacerRepository);
            }
            this.racers.Add(racer); //Does it return success?
        }

    
        public IRacer FindBy(string property) => this.racers.FirstOrDefault(x => x.Username == property);



        public bool Remove(IRacer racer) => this.racers.Remove(racer); //Does it return success?

    }
}
