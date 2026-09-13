using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Estructuras_de_control
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("estructurasdecontrol");
            // secuencial
            string nombre;

            
            Console.WriteLine("ingrese su nombre");
            nombre = Console.ReadLine();
            Console.WriteLine("ingrese edad:");
            int edad = int.Parse(Console.ReadLine());
            Console.WriteLine($"nomnre: {nombre} , Edad : {edad} ");

            // condicional
            if (edad >= 18)
            {
                Console.WriteLine("eres mayor");

            }
            else { 
                 Console.WriteLine("eres menor");

            }

            // repetitivas
            Console.WriteLine("ingresar numero del 1 al 3:");
            int opcion = int.Parse(Console.ReadLine());
            switch (opcion)
            {
                case 1: Console.WriteLine("opcion 1"); break;
                case 2: Console.WriteLine("opcion 2"); break;
                case 3: Console.WriteLine("opcion 3"); break;
                default: Console.WriteLine("opcion invalido"); break;
            }
            // anidado

            if (opcion == 1)
            {
                Console.WriteLine("opcion 1");

            }
            else if (opcion == 2)
            {
                Console.WriteLine("opc 2");

            }
            else if (opcion == 3)
            {
                Console.WriteLine("opc 3");
            }

            }
    }
}
