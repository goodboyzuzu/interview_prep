from enum import Enum, auto


class ConnectionInvitationStatus(Enum):
  PENDING, ACCEPTED, CONFIRMED, REJECTED, CANCELED = 1, auto, 3, 4, 5

print(ConnectionInvitationStatus.ACCEPTED)
print(repr(ConnectionInvitationStatus.ACCEPTED))
print(type(ConnectionInvitationStatus.ACCEPTED))
print(ConnectionInvitationStatus.ACCEPTED.name)