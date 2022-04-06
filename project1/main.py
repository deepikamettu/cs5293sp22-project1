import argparse
import redactor

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("--input", required=True, action='append', type=str)
    parser.add_argument("--names", action='store_true')
    parser.add_argument("--genders", action='store_true')
    parser.add_argument("--dates", action='store_true')
    parser.add_argument("--phones", action='store_true')
    parser.add_argument("--address", action='store_true')
    parser.add_argument("--concept", action='append', type=str)
    parser.add_argument("--stats", type=str,required=True,action ='append')
    parser.add_argument("--output",type=str,required=True)

    args = parser.parse_args()
    
    data = redactor.inputData(args.input)

    if (args.names):
        data = redactor.nameRedaction(data)
    if (args.genders):
        data = redactor.genderRedaction(data)
    if (args.dates):
        data = redactor.dateRedaction(data)
    if (args.concept):
        data = redactor.conceptRedaction(data, args.concept)
    if (args.phones):
        data = redactor.phoneRedaction(data)
    if (args.address):
        data = redactor.addressRedaction(data)
    if (args.output):
        redactor.output(args.input,data)
    if (args.stats):
        redactor.statistics(args.stats)
