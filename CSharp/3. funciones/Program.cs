using Microsoft.VisualBasic;

Console.WriteLine("funciones");

static void saludar ()
{
    Console.WriteLine("Hola, Bienvenido a fundamentos");
}

saludar();

Console.WriteLine("Funciones sin retorno");
 static void menu()
{
    Console.WriteLine("1.registar");
    Console.WriteLine("2.buscar");
    Console.WriteLine("3.salir");
}
menu();

Console.WriteLine("Funciones con retorno");
Console.WriteLine("------------------------");
int resultado = producto(7,8);
Console.WriteLine($"{resultado}, resultado*2={resultado*2}");
static int producto(int a, int b)
{
    return a * b;
}

Console.WriteLine("Funciones con varios argumentos");
Console.WriteLine("------------------------");

static double promedio(double t1, double t2, double t3, double ep, double ef)
{
    return t1*0.1 + t2*0.1 + t3*0.1 + ep*0.2 +ef*0.5;
}

double resultado1 = promedio(20,20,20,14,12);
Console.WriteLine($"promedio obtenido es:{resultado1}");

Console.WriteLine("Funciones con varios parametros predeterminados :)");
Console.WriteLine("------------------------");

static void saludar_estud(string nombre, string curso="fundamentos progra")
{
    Console.WriteLine($"hola {nombre}, bienvenido a {curso}");
}

saludar_estud("pancho");
saludar_estud("pancho","base de datos");

Console.WriteLine("Funciones aniadadas :) XD");
Console.WriteLine("------------------------");

static double proceso_compra(double monto)
{
    double aplicar_igv(double valor)
    {
        return valor*0.18;
    }
    double igv = aplicar_igv(monto);
    double total =monto+ igv;
    return total;
}
double venta = proceso_compra(550);
Console.WriteLine($"total a pagar s/. {venta}");

//funciones con parametros por valor
//--------------------------------

static void incrementar(int numero)
{
    numero = numero + 5;
    Console.WriteLine($"dentro de la funcion: {numero}");
}

int z=25;
incrementar(z);
Console.WriteLine($"fuera de la funcion: {z}");

//funciones con parametros por refderencia
//--------------------------------

static void incrementar_referencia(ref int numero)
{
    numero = numero+10;
    Console.WriteLine($"dentro de la funcion: {numero}");
}

int y =30;
incrementar_referencia(ref y);
 Console.WriteLine($"fuera de la funcion: {y}");











































































































































































































































































































































































































































































































































