#include <ros/ros.h>
#include <geometry_msgs/PoseStamped.h>

#include "via_navigation/RequestGoalPos.h"

geometry_msgs::PoseStamped goal1;
geometry_msgs::PoseStamped goal2;
geometry_msgs::PoseStamped goal3;

ros::Publisher goalPub_;

void initPoseMessages () {

	// Goal 1
	goal1.header.stamp = ros::Time::now();
	goal1.header.frame_id = "odom";

	goal1.pose.position.x =-6.0;
	goal1.pose.position.y = 0.0;
	goal1.pose.position.z = 0.0;

	goal1.pose.orientation.x = 0.0;
	goal1.pose.orientation.y = 0.0;
	goal1.pose.orientation.z = 0.0;
	goal1.pose.orientation.w = 1.0;

	// Goal 2
	goal2.header.stamp = ros::Time::now();
	goal2.header.frame_id = "odom";

	goal2.pose.position.x = 4.0;
	goal2.pose.position.y = -7.5;
	goal2.pose.position.z = 0.0;

	goal2.pose.orientation.x = 0.0;
	goal2.pose.orientation.y = 0.0;
	goal2.pose.orientation.z = 0.0;
	goal2.pose.orientation.w = 1.0;

	// Goal 3
	goal3.header.stamp = ros::Time::now();
	goal3.header.frame_id = "odom";

	goal3.pose.position.x = -7.0;
	goal3.pose.position.y = 7.0;
	goal3.pose.position.z = 0.0;

	goal3.pose.orientation.x = 0.0;
	goal3.pose.orientation.y = 0.0;
	goal3.pose.orientation.z = 0.0;
	goal3.pose.orientation.w = 1.0;
}

bool publishGoalPos(via_navigation::RequestGoalPos::Request  &req,
	   	   	   	    	via_navigation::RequestGoalPos::Response &res)
{
	if (req.data == 1)	{
		goal1.header.stamp = ros::Time::now();
		goalPub_.publish(goal1);
	}
	if (req.data == 2)	{
		goal1.header.stamp = ros::Time::now();
		goalPub_.publish(goal2);
	}
	if (req.data == 3)	{
		goal1.header.stamp = ros::Time::now();
		goalPub_.publish(goal3);
	}

	res.success = true;

	return true;
}

int main(int argc, char** argv)
{
	// Init ROS node
	ros::init(argc, argv, "send_navigation_goals");
	ros::NodeHandle nodeHandle;

	initPoseMessages();

	ros::ServiceServer publishGoalPosSrv = nodeHandle.advertiseService("request_goal_pos", publishGoalPos);

	goalPub_ = nodeHandle.advertise<geometry_msgs::PoseStamped>("/move_base_simple/goal", 100);

  ros::spin();

	return 0;
}
