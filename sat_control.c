#DEFINE MAX_RAD 3;
#DEFINE MAX_THETA 359;

struct polar_coord{//polar coord system. 
	double radius;//radius is equivalent to distance from dish pointed straight up, 
	double theta;//theta is angle in degrees, 0 degrees arbitrarily set to E, increasing CCW towards N
}

void track_start_pos(polar_coord start, polar_coord *curr_pos){//move to predicted/calculated orbit track start
	while(*curr_pos.radius<MAX_RAD){
		*curr_pos.radius++;
	}
	while(*curr_pos.theta!=start.theta){
		if (*curr_pos.theta>start.theta) *curr_pos.theta--;
		else if (*curr_pos.theta<start.theta) *curr_pos.theta++;
	}
}

