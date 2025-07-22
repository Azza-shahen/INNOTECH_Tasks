using System.Text;// for use String Builder 
#region Summation 1 to N using Looping

Console.Write("Enter a number: ");
string? MaxNumberFormUser = Console.ReadLine();

if (!string.IsNullOrWhiteSpace(MaxNumberFormUser) && int.TryParse(MaxNumberFormUser, out int MaxNamber))
{
   
    int sum = 0;
    for (int i = 1; i <= MaxNamber; i++)
    {
        sum += i;
    }
    Console.WriteLine($"[Looping] The sum from 1 to {MaxNamber} is: {sum}");

    // Now use formula for summation
    int sumFromFormula = MaxNamber * (MaxNamber + 1) / 2;
    Console.WriteLine($"[Formula] The sum from 1 to {MaxNamber} is: {sumFromFormula}");

}
else
{
    Console.WriteLine("Invalid input! Please enter a valid integer number.");
}
#endregion

#region Print numbers from 1 to n using StringBuilder (no without last comma)

Console.Write("Enter a number: ");
string? input = Console.ReadLine();

if (!string.IsNullOrWhiteSpace(input) && int.TryParse(input, out int n))
{
    StringBuilder sb = new StringBuilder();

    for (int i = 1; i <= n; i++)
    {
        sb.Append(i);
        if (i < n)
        {
            sb.Append(", ");
        }
    }

    Console.WriteLine($"Numbers from 1 to {n}:");
    Console.WriteLine(sb.ToString());


}
else
{
    Console.WriteLine("Invalid input! Please enter a valid integer.");
}

#endregion

#region Explanation: How StringBuilder works internally 
#region String (Immutable)
/*
    - In C#, string is immutable.
    - Every time you do: str += "something", a new string is created in memory.
    - Example:
        string str = "";
        for (int i = 0; i < 1000; i++)
            str += i.ToString();

    - This creates a new string 1000 times ⇒ very slow and memory-heavy.
    - Time complexity: O(n²)
*/
#endregion

#region StringBuilder (Mutable)
/*
    - StringBuilder is mutable.
    - Internally, it uses a resizable character array (char[] buffer).
    - When you call .Append(), it adds to the buffer instead of creating a new string.
    - If the buffer fills up, it automatically resizes (usually by doubling its size).
    - Time complexity: O(n) amortized.

    - Example:
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 1000; i++)
            sb.Append(i);

    - Only one buffer resize may happen, making it highly efficient.
*/
#endregion

#endregion