import tracker

def main():
    T = tracker.Tracker()
    T._print_debug_get_info_object()
    print T.calculate_current_position()
    print T.calculate_next_position()

if __name__ == '__main__':
    main()

