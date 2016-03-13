import clr
import sys
if sys.platform.lower() not in ['cli','win32']:
    print("only windows is supported for wpf")
try:
    ironpy = sys.implementation.name.lower() == "ironpython"
except:
    ironpy = False
if ironpy:
    import wpf
else:
    clr.AddReference(r"wpf\PresentationFramework")
    from System.IO import StreamReader
    from System.Windows.Markup import XamlReader
    from System.Threading import Thread, ThreadStart, ApartmentState

from System.Windows import Application, Window


class MyWindow(Window):
    def __init__(self):
        if ironpy:
            wpf.LoadComponent(self, "DynamicGrid.xaml")
        else:
            stream = StreamReader("DynamicGrid.xaml")
            window = XamlReader.Load(stream.BaseStream)
            Application().Run(window)
            

if __name__ == '__main__':
    if ironpy:
        Application().Run(MyWindow())
    else:
        thread = Thread(ThreadStart(MyWindow))
        thread.SetApartmentState(ApartmentState.STA)
        thread.Start()
        thread.Join()
