Console.WriteLine("tipos de variabales");

static void saludar()
{
    string nombre = "Juan";
    Console.WriteLine($"Hola, {nombre}, bienvenido a C#");
}

saludar();

//Console.WriteLine("nombre");

Console.WriteLine("variable globla");
int incrementar = 0;
void incrementa()
{
    incrementar += 20;
    Console.WriteLine($"El valor de incrementar es: {incrementar}");
}

incrementa();



Console.WriteLine("variable no local");
static void calcularmonto()
{
    double subtotal = 100;
    double calcular_igv(double a)
    {
        return a * 0.18;
    }
    double resultado = calcular_igv(subtotal);
    Console.WriteLine($"El resultado del igv es: {resultado + subtotal}"); 
}
calcularmonto();
















































