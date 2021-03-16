#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <winSock2.h>
#define _USE_MATH_DEFINES
#include <math.h>

#pragma warning(disable : 4996)
#pragma comment(lib, "ws2_32.lib")

// User and Launcher Information
#define NICKNAME "GUMI03_PARKMOCEE"
#define HOST "127.0.0.1"

// Static Value(Do not modify)
#define PORT 1447
#define CODE_SEND 9901
#define CODE_REQUEST 9902
#define SIGNAL_ORDER 9908
#define SIGNAL_CLOSE 9909

void ErrorHandling(char *message);

int main()
{
	// Predefined Variables(Do not modify)
	int TABLE_WIDTH = 254;
	int TABLE_HEIGHT = 127;
	int NUMBER_OF_BALLS = 6;
	int HOLES[6][2] = {{0, 0}, {127, 0}, {254, 0}, {0, 127}, {127, 127}, {254, 127}};

	int balls[6][2] = {
		0,
	};
	int order = 0;

	WSADATA wsaData;
	SOCKET hSocket;
	SOCKADDR_IN sockAddr;

	if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0)
		ErrorHandling("WSAStartup failure.");

	hSocket = socket(PF_INET, SOCK_STREAM, 0);

	if (hSocket == INVALID_SOCKET)
		ErrorHandling("Socket Creating Failure.");

	memset(&sockAddr, 0, sizeof(sockAddr));
	sockAddr.sin_family = AF_INET;
	sockAddr.sin_addr.s_addr = inet_addr(HOST);
	sockAddr.sin_port = htons(PORT);

	printf("Trying Connect: %s:%d\n", HOST, PORT);
	if (connect(hSocket, (SOCKADDR *)&sockAddr, sizeof(sockAddr)) == SOCKET_ERROR)
		ErrorHandling("Connection Failure.");
	else
		printf("Connected: %s:%d\n", HOST, PORT);

	char sendData[50];

	sprintf(sendData, "%d/%s/", CODE_SEND, NICKNAME);
	send(hSocket, (char *)&sendData, sizeof(sendData), 0);
	printf("Ready to play!\n--------------------");

	while (1)
	{
		char message[50];
		int strLen;

		strLen = recv(hSocket, message, sizeof(message) - 1, 0);

		char *recvData;
		recvData = strtok(message, "/");
		int pos = atoi(recvData);

		for (int i = 0; i < NUMBER_OF_BALLS; i++)
		{
			for (int j = 0; j < 2; j++)
			{
				balls[i][j] = pos;
				recvData = strtok(NULL, "/");

				if (recvData != NULL)
				{
					pos = atoi(recvData);
				}
			}
		}

		if (balls[0][0] == SIGNAL_ORDER)
		{
			order = balls[0][0];
			printf("\n\n* You will be the %s player. *\n\n", order == 1 ? "first" : "second");
			continue;
		}
		else if (balls[0][0] == SIGNAL_CLOSE)
		{
			break;
		}

		for (int i = 0; i < NUMBER_OF_BALLS; i++)
		{
			printf("ball %d: %d, %d\n", i, balls[i][0], balls[i][1]);
		}

		float angle = 0.0f;
		float power = 0.0f;

		//////////////////////////////
		// Begining of Your Code
		// Put your code here to set angel and power values.
		// angle(float) must be between 0.0 and 360.0
		// power(float) must be between 1.0 and 100.0
		int whiteBall_x = balls[0][0];
		int whiteBall_y = balls[0][1];

		int targetBall_x = balls[1][0];
		int targetBall_y = balls[1][1];

		int width = abs(targetBall_x - whiteBall_x);
		int height = abs(targetBall_y - whiteBall_y);

		double radian = atan(width / height);
		angle = (float)((180 / M_PI) * radian);

		if (targetBall_y < whiteBall_y)
		{
			radian = atan(height / width);
			angle = (float)(((180 / M_PI) * radin) + 90);
		}

		double distance = (double)sqrt((width * width) + (height * height));

		power = (float)distance;
		// You can clear Stage 1 with the pre-written code above.
		// Those will help you to figure out how to clear other Stages.
		// Good luck!!
		// End of Your Code
		//////////////////////////////

		char mergedData[50];
		sprintf(mergedData, "%f/%f/", angle, power);
		send(hSocket, (char *)&mergedData, sizeof(mergedData), 0);
		printf("Data Sent: %s\n", mergedData);
	}

	closesocket(hSocket);
	WSACleanup();

	return 0;
}

void ErrorHandling(char *message)
{
	fputs(message, stderr);
	fputc('\n', stderr);
	exit(1);
}