import src.data_generate_jongrin as jr



data = []

data.extend(jr.gen_data())


print(len(data))
print(data[:5])
print(data[-3:])
