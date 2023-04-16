import organizeFolder as organizeFolder
import os
import shutil
import argparse
import textwrap
import resize_image as resize_image
import logoaddimage as logoaddimage
import youtube_download as ytd
import splitpdf
def main():
    parser = argparse.ArgumentParser(
                    prog='Auto Operation',
                    description=textwrap.dedent('''\
        Please do not mess up this text!
        --------------------------------
            1-organiz Folder
            2-resize Image
            3-Put logo on image
            4-download youtube video 
            5-download playlist video
            6-split pdf to pages
        '''),
                    epilog='')
    parser.print_help()
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-o", "--operation", help="your name")
    argParser.add_argument("-p", "--path", help="your name")
    argParser.add_argument("-u", "--out_folder", help="your name")
    argParser.add_argument("-s", "--sizeimage", help="your name")
    argParser.add_argument("-r", "--psizeimage", help="your name")
    argParser.add_argument("-l", "--logoname", help="your name")
    argParser.add_argument("-ps", "--postionlogo", help="your name")
    argParser.add_argument("-url", "--youtubvideo", help="your name")
    argParser.add_argument("-f", "--filepdf", help="your name")
    argParser.add_argument("-start", "--start_page", help="your name")
    argParser.add_argument("-end", "--end_page", help="your name")
    args = argParser.parse_args()
    isValid=True;
    global current_dir
    if args.path is not None:
         organizeFolder.current_dir=args.path
    global out_folder
    if args.out_folder is not None:
         organizeFolder.out_folder=args.out_folder
    if args.operation is  None:
         print( "you Must enter Operation")
         isValid=False
    else:
        match args.operation:
            case "1":
                if isValid:
                    organizeFolder.organizAllfill()

                    print("done Organize")
            case "2":
                  if args.out_folder is not None:
                        resize_image.out_folder=args.out_folder
                  if args.path is not None:
                        resize_image.current_dir=args.path
                  if args.psizeimage is not None:
                        resize_image.percent=int(args.psizeimage)
                  if args.sizeimage is not None:
                        resize_image.fite_size=int(args.sizeimage)
                  if args.sizeimage is None and args.psizeimage is None:
                        isValid=False
                        print("You Must Set Size Image -s <size>\n Or set percent -r <percent>")
                  if isValid:
                    
                    resize_image.resize()
            case "3":
                   if args.out_folder is not None:
                        logoaddimage.out_folder=args.out_folder
                   if args.path is not None:
                        logoaddimage.current_dir=args.path
                   if args.logoname is not None:
                        logoaddimage.logo_file=args.logoname
                   if args.postionlogo is not None:
                        logoaddimage.position=args.postionlogo
                   logoaddimage.add_logo_image()
            case "4":
                    if args.youtubvideo is None :
                        isValid=False
                        print("you must set url video -url <youtube link1>")
                    if args.path is not None:
                        ytd.current_dir=args.path
                    if isValid:
                         ytd.url_video=args.youtubvideo
                         ytd.download_video()
            case "5":
                    if args.youtubvideo is None :
                        isValid=False
                        print("you must set url video -url <youtube link1>")
                    if args.path is not None:
                        ytd.current_dir=args.path
                    if isValid:
                         ytd.url_video=args.youtubvideo
                         ytd.download_playlist()
            case "6":
                    if args.filepdf is None :
                        isValid=False
                        print("you must set pdf -f <pdf path>")
                    if args.path is not None:
                        splitpdf.file=args.path
                    if args.start_page is not None:
                        splitpdf.start=int(args.start_page)
                    if args.end_page is not None:
                        splitpdf.endp=int(args.end_page)
                    if isValid:
                         splitpdf.file=args.filepdf
                         splitpdf.split_pdf();
            case "7":
                    if args.filepdf is None :
                        isValid=False
                        print("you must set pdf -f <pdf path>")
                    if args.path is not None:
                        splitpdf.file=args.path
                    if args.logoname is not None:
                        splitpdf.logo_file=int(args.logoname)
                    
                    if isValid:
                         splitpdf.file=args.filepdf
                         splitpdf.add_whater_mark();
            case _:
                  print( "envalid option")

if __name__ == "__main__":
    main()