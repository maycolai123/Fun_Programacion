using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Fundamentos
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("fundamenos de csharp");
            Console.WriteLine("tipos de datos");
            //1. numero entero
            int edad = 25;

            //2. cadena de texto
            string nombre = "maycol";

            //3. numero decimal
            double precio = 19.99;

            //4. valor logico
            bool estado = false;

            //5. valor caracter
            char genero = 'M';

            Console.WriteLine("entrada-salida-comentarios");
            //entrada
            Console.Write("ingrese su nombre");
            nombre = Console.ReadLine();

            // salida
            Console.WriteLine($"hola, {nombre}");

            //comentario linea

            /*
             *comentaro bloque
             
             */
            // ejecutar un programa visual estudio code
            dotnet run 

        

        }
    }
}

