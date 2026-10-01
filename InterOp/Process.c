__declspec(dllexport)
void process(int *input, int *output, int size)
{
    for (int i = 0; i < size; i++)
    {
        output[i] = input[i] * 2;
    }
}