using System;
using System.Collections.Generic;
using System.Text;
using System.Linq;


namespace SkiRental
{
    class SkiRental
    {

        List<Ski> skis;
        

        public SkiRental(string name, int capacity)
        {
            Capacity = capacity;
            skis = new List<Ski>();
            Name = name;
        }

        public int Capacity { get; set; }
        public string Name { get; set; }
        public int Count => skis.Count;

        public void Add(Ski ski) //Method
        {
            if (Capacity > Count)
            {
                skis.Add(ski);
            }

        }

        public bool Remove(string manufacturer, string model) //Method
        {
                            return skis.Remove(skis.FirstOrDefault(x => x.Manufacturer == manufacturer && x.Model == model));

               
         
        }

        public Ski GetNewestSki()
        {
            if (Count > 0)
            {
                int maxy = 0;
                string mcurman = "";
                string mcurmodel = "";
                foreach (Ski ski in skis)
                {
                    if (ski.Year> maxy)
                    {
                        maxy = ski.Year;
                        mcurman = ski.Manufacturer;
                        mcurmodel = ski.Model;
                    }
                }
                foreach (Ski ski in skis)
                {
                    if (ski.Year == maxy)
                    {
                        return ski;
                    }
                }
                
            }
            return null;
        }

       public Ski GetSki(string manufacturer, string model)
        {
            foreach (Ski ski in skis)
            {
                if (ski.Manufacturer == manufacturer && ski.Model==model)
                {
                    return ski;
                }
            }
            return null;
        }

        public string GetStatistics()
        {

            var sb = new StringBuilder();
            sb.AppendLine($"The skis stored in " + this.Name + ":");
            foreach (Ski ski in skis)
            {
                sb.AppendLine($"{ski.Manufacturer} - {ski.Model} - {ski.Year}");
            }
            return sb.ToString();
        }

    }
}
