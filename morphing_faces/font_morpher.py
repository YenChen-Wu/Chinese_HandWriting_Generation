import numpy

numpy.random.seed(112387)


class Morpher(object):
    # Shape of the generated images
    image_shape = (100, 100)

    def __init__(self):
        # If true, ignore requests to change the coordinates of Z
        self.freeze_coordinates = False
        # Dimensions along which coordinates of Z will vary
        self.dimension_0 = 0
        self.dimension_1 = 1
        # Point in latent space, selected at random to begin with
        self.Z = self._sample_Z()

        # Model parameters
        f=file('../Variational-Autoencoder/trained_params','rb')
        [self.W1,self.W2,self.W3,self.W4,self.W5,self.W6,self.b1,self.b2,self.b3,self.b4,self.b5,self.b6] = cPickle.load(f)

    def toggle_freeze(self):
        """
        Toggles on and off the option to ignore requests to change coordinates
        of Z
        """
        self.freeze_coordinates = not self.freeze_coordinates

    def _sample_Z(self):
        """
        Samples a point in latent space according to the prior distribution
        p(Z)
        """
        return numpy.random.normal(size=(20, ))

    def shuffle(self):
        """
        Resamples a new Z
        """
        self.Z = self._sample_Z()

    def select_dimensions(self, d_0, d_1):
        """
        Selects the two dimensions in Z along which coordinates will vary
        """
        if d_0 not in self.index_mapping or d_1 not in self.index_mapping:
            raise KeyError()
        self.dimension_0 = d_0
        self.dimension_1 = d_1

    def get_Z(self):
        """
        Returns the current point in latent space
        """
        return self.Z.copy()

    def set_Z(self, Z):
        """
        Sets the current point in latent space
        """
        self.Z = Z.copy()

    def set_coordinates(self, x, y):
        """
        Sets new coordinates for the two selected dimensions of Z if
        coordinates are not frozen
        """
        if not self.freeze_coordinates:
            self.Z[self.dimension_0] = x
            self.Z[self.dimension_1] = y

    def generate_face(self):
        """
        Maps the point Z in latent space to a 48 x 48 pixels face image
        """
        h_decoder = T.tanh(T.dot(self.W4, self.Z) + self.b4)
        X = T.nnet.sigmoid(T.dot(self.W5,h_decoder) + self.b5)

        #A_2 = numpy.dot(self.Z, self.d_W_2) + self.d_b_2
        #H_2 = numpy.where(A_2 > 0.0, A_2, 0.0 * A_2)
        #A_1 = numpy.dot(H_2, self.d_W_1) + self.d_b_1
        #H_1 = numpy.where(A_1 > 0.0, A_1, 0.0 * A_1)
        #A_0 = numpy.dot(H_1, self.d_W_0) + self.d_b_0
        #X = 1.0 / (1.0 + numpy.exp(-A_0))

        return X.reshape(self.image_shape)

    def infer_Z(self, X):
        """
        Maps an 48 x 48 face image to its representation Z in latent space

        Parameters
        ----------
        X : numpy.array
            Array of shape (2304, ) or (48, 48) representing the face image
        """
        h_encoder = T.tanh(T.dot(W1,x) + b1)
        mu_encoder = T.dot(W2,h_encoder) + b2
        log_sigma_encoder = 0.5*(T.dot(W3,h_encoder) + b3)
        z = mu_encoder + T.exp(log_sigma_encoder)*eps
        
        #A_1 = numpy.dot(X, self.e_W_0) + self.e_b_0
        #H_1 = numpy.where(A_1 > 0.0, A_1, 0.0 * A_1)
        #A_2 = numpy.dot(H_1, self.e_W_1) + self.d_b_1
        #H_2 = numpy.where(A_2 > 0.0, A_2, 0.0 * A_2)
        #Z = numpy.dot(H_2, self.e_W_2) + self.e_b_2

        return Z
