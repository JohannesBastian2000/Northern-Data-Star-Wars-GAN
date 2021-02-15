from GenerateDataset import GenerateDataset


dataset_generator = GenerateDataset(
    every_x_frame=13,
    video_urls=[
        "https://www.youtube.com/watch?v=tTDnOwvhkts&list=PLhcUoUk1kLVwK73QKzD_h7sTV9aqe15jx&index=86",
        "https://www.youtube.com/watch?v=tjzaDF2q0TE&list=PLhcUoUk1kLVwK73QKzD_h7sTV9aqe15jx&index=87",
        "https://www.youtube.com/watch?v=ghOzwa3Dh0w&list=PLhcUoUk1kLVwK73QKzD_h7sTV9aqe15jx&index=88",
        "https://www.youtube.com/watch?v=Oz3wpkCt2Ms&list=PLhcUoUk1kLVwK73QKzD_h7sTV9aqe15jx&index=89",
        "https://www.youtube.com/watch?v=WOHJgoW5OCg&list=PLhcUoUk1kLVwK73QKzD_h7sTV9aqe15jx&index=90",
        "https://www.youtube.com/watch?v=7J9-e_VeaZ8&list=PLhcUoUk1kLVwK73QKzD_h7sTV9aqe15jx&index=92",
        "https://www.youtube.com/watch?v=-E9yeLhIvn8&list=PLhcUoUk1kLVwK73QKzD_h7sTV9aqe15jx&index=93",
        "https://www.youtube.com/watch?v=A9xZJpsqOfE&list=PLhcUoUk1kLVwK73QKzD_h7sTV9aqe15jx&index=94",
        "https://www.youtube.com/watch?v=iK7LXyMdUW4&list=PLhcUoUk1kLVwK73QKzD_h7sTV9aqe15jx&index=96",
        "https://www.youtube.com/watch?v=ss1nFJC197M&list=PLhcUoUk1kLVwK73QKzD_h7sTV9aqe15jx&index=97",
        "https://www.youtube.com/watch?v=_z1s1vAVXEQ&list=PLhcUoUk1kLVwK73QKzD_h7sTV9aqe15jx&index=99",
        "https://www.youtube.com/watch?v=N8f3-QPBxUA&list=PLhcUoUk1kLVwK73QKzD_h7sTV9aqe15jx&index=101",
        "https://www.youtube.com/watch?v=b4KqMxlWA0I&list=PLhcUoUk1kLVwK73QKzD_h7sTV9aqe15jx&index=102",
        "https://www.youtube.com/watch?v=XTO2JldWAL0&list=PLhcUoUk1kLVwK73QKzD_h7sTV9aqe15jx&index=103",
        "https://www.youtube.com/watch?v=ciMbuvfSQtk&list=PLhcUoUk1kLVwK73QKzD_h7sTV9aqe15jx&index=104",
        "https://www.youtube.com/watch?v=7q2TNPxSxj0&list=PLhcUoUk1kLVwK73QKzD_h7sTV9aqe15jx&index=105",
        "https://www.youtube.com/watch?v=qI1UcARiOvM&list=PLhcUoUk1kLVwK73QKzD_h7sTV9aqe15jx&index=106",
        "https://www.youtube.com/watch?v=KodF2w1JMwQ&list=PLhcUoUk1kLVwK73QKzD_h7sTV9aqe15jx&index=107",
        "https://www.youtube.com/watch?v=hV6YJau5xTA&list=PLhcUoUk1kLVwK73QKzD_h7sTV9aqe15jx&index=108",
        "https://www.youtube.com/watch?v=hLLBZsEtuUs&list=PLhcUoUk1kLVwK73QKzD_h7sTV9aqe15jx&index=109",
        "https://www.youtube.com/watch?v=1Y_8QDBBnrU&list=PLhcUoUk1kLVwK73QKzD_h7sTV9aqe15jx&index=110",
        "https://www.youtube.com/watch?v=T-aX-vFKcC8&list=PLhcUoUk1kLVwK73QKzD_h7sTV9aqe15jx&index=111",
        "https://www.youtube.com/watch?v=Qcd2YkfF8Ag&list=PLhcUoUk1kLVwK73QKzD_h7sTV9aqe15jx&index=112",
        "https://www.youtube.com/watch?v=GZz6GQT0o8I&list=PLhcUoUk1kLVwK73QKzD_h7sTV9aqe15jx&index=113",
        "https://www.youtube.com/watch?v=W7zZGTmghrE&list=PLhcUoUk1kLVwK73QKzD_h7sTV9aqe15jx&index=114",
        "https://www.youtube.com/watch?v=DhLgvrAwTUE&list=PLhcUoUk1kLVwK73QKzD_h7sTV9aqe15jx&index=115",
        "https://www.youtube.com/watch?v=RvamRJvAB2U&list=PLhcUoUk1kLVwK73QKzD_h7sTV9aqe15jx&index=116",
        "https://www.youtube.com/watch?v=HRhWD-M08mw&list=PLhcUoUk1kLVwK73QKzD_h7sTV9aqe15jx&index=117",
    ],
)
dataset_generator.run()
