using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace semana_3
{
    internal class Program
    {
        static void Main(string[] args)//funcion PRINCIPAL
        {
            for (int i = 0; i < 6; i++)
                Console.Beep(900,500);
                Console.Clear();//limpiar consola
            Console.ReadKey();//detener hasta que escribas algo

            RegistrarDatos();
             } 
        //FUNCION 1
        static void RegistrarDatos() {
                Console.WriteLine("ingrese su nombre");
                string nombre = Console.ReadLine(); // JUAN PEREZ

                Console.WriteLine("ingrese su edad");
                int edad = int.Parse(Console.ReadLine());//19 21
            DeterminarMayorEdad(edad);
        }
        //FUNCION 2
        static void DeterminarMayorEdad(int edad) {
                if (edad >= 18)
                {
                    Console.WriteLine("eres mayor de edad, puedes salir a alcoholizarte con tus reales: EMILIO");
                }
                else
                {
                    Console.WriteLine("no eres mayor de edad");
                }
            }
        



    }
}
