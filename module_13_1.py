import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
        for i in range(1, 6):
        print(f'Силач {name} поднял {i} шар')
            if i == 5:
                print(f'Силач {name} закончил соревнования')
            await asyncio.sleep(power)
            
async def start_tournamen():
    name1 = asyncio.create_task(start_strongman('Pasha', 3))
    name2 = asyncio.create_task(start_strongman('Denis', 4))
    name3 = asyncio.create_task(start_strongman('Apollon', 5))
    await name1
    await name2
    await name3


asyncio.run(start_tournamen())
=>
Силач Pasha начал соревнования.
Силач Pasha поднял 1 шар
Силач Denis начал соревнования.
Силач Denis поднял 1 шар
Силач Apollon начал соревнования.
Силач Apollon поднял 1 шар
Силач Pasha поднял 2 шар
Силач Denis поднял 2 шар
Силач Apollon поднял 2 шар
Силач Pasha поднял 3 шар
Силач Denis поднял 3 шар
Силач Pasha поднял 4 шар
Силач Apollon поднял 3 шар
Силач Denis поднял 4 шар
Силач Pasha поднял 5 шар
Силач Pasha закончил соревнования
Силач Apollon поднял 4 шар
Силач Denis поднял 5 шар
Силач Denis закончил соревнования
Силач Apollon поднял 5 шар
Силач Apollon закончил соревнования

Process finished with exit code 0
