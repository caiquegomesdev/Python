using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Banco
{
    class Program
    {
        static void Main(string[] args)
        {
            // Cria uma conta corrente
            var contaCorrente = new ContaCorrente("1234-5678-9012-3456", 1000.0);

            // Deposita 500 reais na conta
            contaCorrente.Depositar(500.0);

            // Sacar 200 reais da conta
            contaCorrente.Sacar(200.0);

            // Imprime o saldo da conta
            Console.WriteLine("Saldo da conta: {0}", contaCorrente.Saldo);
        }
    }
}