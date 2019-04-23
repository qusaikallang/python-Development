def main():
            data = "First probably one of the most challenging things you can do on a computer (next to killing the final boss in Doom on Nightmare difficulty level). Composing an operating system requires a lot of knowledge about several complex areas within computer science. You need to understand how hardware works, be able to read and write the complex Assembly language, and also a higher level language (like for instance C, C++ or Pascal). Your mind has to be able to wrap itself around abstract theory, and hold a myriad of thoughts. Feel discouraged yet? Don't fear! Because all of these things are also the things that makes OS programming fun and entertaining"
            #data = input("Input data to be trimmed")
            start = input("The starting point of cutting process")
            End = input("The end point of cutting process")
            res = ''
            seg = data.split(" ")
            trash = []
            i = 0
            st = 0
            ed = 0
            for line in seg:
                if start in line:
                    st = seg.index(line)
                if End in line:
                    ed = seg.index(line)

            while st <= ed:
                trash.append(seg.pop(ed))
                ed-=1
            res = ' '.join(seg)
            trash = ' '.join(trash)
            print(res)
            print(trash)

if __name__ == '__main__':
            main()
