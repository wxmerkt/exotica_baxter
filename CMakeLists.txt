cmake_minimum_required(VERSION 2.8.3)
project(exotica_baxter)

find_package(catkin REQUIRED)

catkin_package(
 CATKIN_DEPENDS baxter_description exotica
)

#############
## Install ##
#############

install(DIRECTORY config/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

install(DIRECTORY launch/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
