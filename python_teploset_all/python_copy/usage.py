import shutil

total, used, free = shutil.disk_usage("N:/")
ds = '―' * 29
Used_Gb = "used: %d Gb" % (used // (2**30))
Free_Gb = "free: %d Gb" % (free // (2**30))
Total_Gb = "total: %d Gb" % (total // (2**30))
mem_info = f'{ds}\nN:// {Total_Gb}\t{Free_Gb} {Used_Gb}\n{ds}'